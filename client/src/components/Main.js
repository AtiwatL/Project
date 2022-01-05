import React, { useState, useEffect } from 'react'
import logo from '../rf.png'
import useRecorder from "./useRecorder";
import './Main.css'

function randText() {
    return (Math.random() + 1).toString(36).substring(7);
}

function Main() {

    const random = () => {
        setRandom(randText())
    }

    const [text, setRandom] = useState("");
    let [audioURL, isRecording, startRecording] = useRecorder();

    return (
        <div className="container">
            <div className="captchaHeading">Voice CAPTCHA | ยืนยันมนุษย์ด้วยเสียง</div>
            <div className="captchaBackground">
                <h1 className = "textSub">กรุณากด RECORD และพูดชุดคำต่อไปนี้</h1>
                <h1 className = "ranText" >{text}</h1>
                <button onClick={random}>
                    <span>
                        <img src={logo} width="10px" height="10px" alt="" />
                    </span>
                </button>
                <button onClick={startRecording} disabled={isRecording} className="textBox">
                    <span>record</span>
                </button>
                <audio src={audioURL} controls />
            </div>
        </div>
    )
}

export default Main
