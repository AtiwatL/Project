import React from 'react'
import './Main.css'
import iconx from '../x.png'

function Bot() {
    return (
        <div className="container">
            <div className="captchaHeading">Voice CAPTCHA | ยืนยันมนุษย์ด้วยเสียง</div>
            <div className="captchaBackground">
                <span>
                    <img src={iconx} width="20px" height="20px" alt=""/>
                </span>
                <h1 className="botCaptcha">
                    Bot
                </h1>
            </div>
        </div>
    )
}

export default Bot
