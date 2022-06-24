import React from 'react'
import Head from "next/head";
import Buttons from './Buttons';
import ButtonHover from './ButtonsHover';
import ButtonOutline from './ButtonsOutline'


const ButtonContainer = () => {
    return (
        <div>
             <Head>
                <title>
                    Design Kit
                </title>
                <meta name="vieport" content="width=device-width, inital-scale=1.0"/>
            </Head>

            <div>
                <hr />
                    <div>
                        <h2>Buttons</h2>
                            <Buttons/>
                    </div>

                <hr />
                    <div>
                        <h2>Outlines</h2>
                            <ButtonOutline/>
                    </div>

                <hr />
                    <div>
                        <h2>Effects</h2>
                            <ButtonHover/>
                    </div>
                <hr />

            </div>
            
        </div>
    )
}

export default ButtonContainer
