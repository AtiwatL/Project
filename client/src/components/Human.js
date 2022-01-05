import React from 'react'
import './Main.css'
import iconcheck from '../check.png'

function Human() {
    return (
        <div className="container">
            <div className="captchaHeading">Voice CAPTCHA | ยืนยันมนุษย์ด้วยเสียง</div>
            <div className="captchaBackground">
                <span>
                    <img src={iconcheck} width="20px" height="20px" alt=""/>
                </span>
                <h1 className="humanCaptcha">
                    HUMAN
                </h1>
            </div>
        </div>
    )
}

export default Human
