package com.example.janken

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.ImageButton
import com.example.janken.databinding.ActivityMainBinding


class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        //setContentView(R.layout.activity_main)

        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        //val gu = findViewById<ImageButton>(R.id.gu)
        //val choki = findViewById<ImageButton>(R.id.choki)
        //val pa = findViewById<ImageButton>(R.id.pa)

        binding.gu.setOnClickListener{ onJankenButtonTapped(it) }
        binding.choki.setOnClickListener { onJankenButtonTapped(it) }
        binding.pa.setOnClickListener { onJankenButtonTapped(it) }
    }

    fun onJankenButtonTapped(view: View?) {
        val intent = Intent(this, ResultActivity::class.java)
        intent.putExtra("MY_HAND", view?.id)
        startActivity(intent)
    }
}