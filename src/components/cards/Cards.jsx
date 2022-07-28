import React from 'react';
import './cards.css'

function Cards(props) {
    return (
        <div className='card'>
            <div className='card__body'>
                <img src={props.img} className='card__img' alt='...'/>
                <p className='card__text'>{props.text}</p>
            </div>
        </div>
    );
}

export default Cards;