import React from 'react';
import { Box, Layer, Button, Main, Heading, Form, FormField, TextInput } from 'grommet';
// import SpotifyLogin from 'react-spotify-login';


class Home extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            loginPopup: false,
        };

    }

    spotifySuccess = (response) => console.log(response);
    spotifyFailure = (response) => console.error(response);

    componentDidMount() {
        document.body.style.backgroundColor = "#3D138D";
    }

    spotifyLogin = (clientId, callback) => {

        const redirect_uri = "http://52.186.154.73:3000/callback/";
        var scopes = 'user-read-private user-read-email';
        let req = `https://accounts.spotify.com/authorize?client_id=${clientId}&response_type=token&redirect_uri=${redirect_uri}&scope=${encodeURIComponent(scopes)}&show_dialog=true`;
        let popup = window.open(req,"_self",
            'Login with Spotify', 'width=800,height=600' );

        var popupToken = popup.location.href;
        console.log(popupToken);
        // popup.close();
    }

    spotifyCallback = (popup, payload) => {
        popup.close();

        fetch('https://api.spotify.com/v1/me', {
            headers: {
                'Authorization': `Bearer ${payload}`
            }
        }).then(response => {
            return response.json()
        }).then(data => {
            // do something with data
        })
    }

    render() {
        return (
            <Box>
                <center>
                    <Box border={{ color: 'brand', size: 'large' }} background={{ color: 'white' }}>
                        <Main pad="large">
                            <Heading>Viber</Heading>
                            <Button primary label="Login" onClick={() => this.spotifyLogin('b02cf49b409b48e78efee8ff058c1687', this.spotifyCallback)} />
                        </Main>
                    </Box>
                </center>


                {/* <SpotifyLogin clientId="b02cf49b409b48e78efee8ff058c1687"
                    redirectUri="localhost:3000"
                    onSuccess={this.spotifySuccess}
                    onFailure={this.spotifySuccess}
                /> */}



                {/* {this.state.loginPopup &&
                    <Layer onEsc={() => this.setState({ loginPopup: false })} onClickOutside={() => this.setState({ loginPopup: false })}>
                        <Login/>
                    </Layer>
                } */}

            </Box>
        )
    }

}

function Login() {
    return (

        <Form onSubmit={({ value }) => { }}>
            <Box margin="xlarge">

                <FormField name="name" htmlfor="textinput-id" label="username">
                    <TextInput id="textinput-id" name="name" />
                </FormField>

                <FormField name="name" htmlfor="textinput-id" label="password">
                    <TextInput id="textinput-id" name="name" />
                </FormField>

                <Box gap="small">
                    <Button type="submit" primary label="Submit" />
                    <Button type="reset" label="Create Account" />
                </Box>
            </Box>

        </Form>
    );
}
export default Home;