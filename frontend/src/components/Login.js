import React, { useState, useEffect } from 'react';
import { Heading, Main, Paragraph } from 'grommet';
import { Redirect } from "react-router-dom";
import axios from 'axios'

function Login(props) {

    const [heading, setHeading] = useState("waiting...");
    const [redirect, setRedirect] = useState("");

    
    // Similar to componentDidMount and componentDidUpdate:
    useEffect(() => {
        //check if the name has access token
        let url = window.location.hash;
        var access_token = new URLSearchParams(url).get('#access_token');

        if (access_token) {
            //redirect to next screen
            props.updateUserToken(access_token);
            setRedirect("/userinfo");
        } else {
            setHeading("Failed to Login");
        }
    });

    if (redirect) {
        return <Redirect to={redirect} />
    }

    return (
        <div>
            <center>
                <Main pad="large">
                    <Heading>Login Status:</Heading>
                    <Paragraph>{heading}</Paragraph>
                </Main>
            </center>
        </div>
    );

    

}

export default Login;

