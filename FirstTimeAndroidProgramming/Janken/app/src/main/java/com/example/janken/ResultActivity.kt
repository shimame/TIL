package com.example.janken

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.example.janken.databinding.ActivityResultBinding
import androidx.datastore.core.DataStore
import androidx.datastore.preferences.createDataStore
import androidx.datastore.preferences.core.Preferences

class ResultActivity : AppCompatActivity() {
    private lateinit var binding: ActivityResultBinding

    lateinit var dataStore: DataStore<Preferences>

    val gu = 0
    val choki = 1
    val pa = 2
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        //setContentView(R.layout.activity_result)
        binding = ActivityResultBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val id = intent.getIntExtra("MY_HAND", 0)

        val myHand: Int
        myHand = when(id) {
            R.id.gu -> {
                binding.myHandImage.setImageResource(R.drawable.gu)
                gu
            }
            R.id.choki -> {
                binding.myHandImage.setImageResource(R.drawable.choki)
                choki
            }
            R.id.pa -> {
                binding.myHandImage.setImageResource(R.drawable.pa)
                pa
            }
            else -> gu
        }

        //コンピュータの手を決める
        val comHand = (Math.random() * 3).toInt()
        when(comHand) {
            gu -> binding.comHandImage.setImageResource(R.drawable.com_gu)
            choki -> binding.comHandImage.setImageResource(R.drawable.com_choki)
            pa -> binding.comHandImage.setImageResource(R.drawable.com_pa)
        }

        //勝敗を判定する
        val gameResult = (comHand - myHand + 3) % 3
        when(gameResult) {
            0 -> binding.resultLabel.setText(R.string.result_draw) //引き分け
            1 -> binding.resultLabel.setText(R.string.result_win)  //買った場合
            2 -> binding.resultLabel.setText(R.string.result_lose) //負けた場合
        }
        binding.backButton.setOnClickListener { finish() }
    }

    private fun saveData(myHand: Int, comHand: Int, gameResult: Int) {
        val pref = createDataStore(name = "preferences")
        //val pref = PreferenceManager.getSharedPreferences(this)
        val gameCount = pref.getInt("GAME_COUNT", 0)
        val winningStreakCount = pref.getInt("WINNING_STREAK_COUNT", 0)
        val lastComHand = pref.getInt("LAST_COM_HAND", 0)
        val lastGameResult = pref.getInt("GAME_RESULT", -1)

        val edtWinningStreakCount: Int =
            when {
                lastGameResult == 2 && gameResult == 2 ->
                    winningStreakCount + 1
                else ->
                    0
            }
        val editor = pref.edit()
        editor.putInt("GAME_COUNT", gameCount + 1)
              .putInt("WINNING_STREAK_COUNT", edtWinningStreakCount)
              .putInt("LAST_MY_HAND", myHand)
              .putInt("LAST_COM_HAND", comHand)
              .putInt("BEFORE_LAST_COM_HAND", lastComHand)
              .putInt("GAME_RESULT", gameResult)
              .apply()

    }
}