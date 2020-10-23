import React from 'react';
import { Box, Layer, Button, Main, Heading, Form, FormField, TextInput } from 'grommet';



class Home extends React.Component {

    constructor(props) {
        super(props);
        this.state = { loginPopup: false };
    }

    componentDidMount() {
        document.body.style.backgroundColor = "#DADADA";
    }

    render() {
        return (
            <Box>
                <center>
                    <Box  border={{ color: 'brand', size: 'large' }} background={{ color: 'white' }}>
                        <Main pad="large">
                            <Heading>Viber</Heading>
                            <Button primary label="Login" onClick={() => this.setState({ loginPopup: true })} />
                        </Main>
                    </Box>
                </center>

                {this.state.loginPopup &&
                    <Layer onEsc={() => this.setState({ loginPopup: false })} onClickOutside={() => this.setState({ loginPopup: false })}>
                        <Login />
                    </Layer>
                }

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