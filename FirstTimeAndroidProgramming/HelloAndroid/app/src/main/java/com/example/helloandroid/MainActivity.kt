package com.example.helloandroid

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.example.helloandroid.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        //setContentView(R.layout.activity_main)

        binding = ActivityMainBinding.inflate(layoutInflater)
        val view = binding.root
        setContentView(view)

        binding.tapHere.setOnClickListener {
            binding.textView.text = "ボタンがタップされました"
        }
    }
}