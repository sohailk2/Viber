import React from 'react';
import { Box, Layer, Button, Main, Heading, Form, FormField, TextInput } from 'grommet';
import axios from 'axios';



class Search extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            formData: "",
            playlist: null
        };
    }

    componentDidMount() {
        axios.get(`http://127.0.0.1:8000/viber/search/`)
            .then(res => {
                console.log(res.data.data);
                this.setState({playlist : res.data.data})
        });

    }

    submitForm = () => {
        this.setState({
            playlist: [
                { name: "song1", artist: "artist1" }, { name: "song2", artist: "artist2" }, { name: "song3", artist: "artist3" }, { name: "song4", artist: "artist4" },
                // {name: "song1", artist: "artist1"},{name: "song1", artist: "artist1"},{name: "song1", artist: "artist1"},{name: "song1", artist: "artist1"}
            ]
        })
    };

    render() {

        if (this.state.playlist == null) {
            return (


                <Form
                    value={this.state.value}
                    onChange={nextValue => this.setState({ formData: nextValue })}
                    onReset={() => this.setState({ value: "" })}
                    onSubmit={({ value }) => { }}
                >
                    <FormField name="name" htmlfor="text-input-id" label="Enter a song name!">
                        <TextInput id="text-input-id" name="name" />
                    </FormField>

                    <Box direction="row" gap="medium">
                        <Button type="submit" primary label="Submit" onClick={() => this.submitForm()} />
                        <Button type="reset" label="Reset" />
                    </Box>

                </Form>

            );
        } else {

            // display the pklaylist
            return (

                <div>
                    <Box
                        overflow="scroll"
                        direction="column"
                        border={{ color: 'brand', size: 'large' }}
                        pad="small"
                        style={{ width: "500px", /**height: '500px'**/ }}
                    >
                        {this.state.playlist.map((song, index) => (
                            <Box margin="xxsmall" pad="small" background="light-3">
                                <h2>{song.name}</h2>

                                <Box direction="row">
                                    <Box pad={{ right: "55px" }}>{song.artist}</Box>
                                    <Box>click</Box>
                                </Box>
                            </Box>
                        ))}
                    </Box>
                    <Button margin="large" type="reset" label="Reset" onClick={() => this.setState({ playlist: null })} />
                </div>

            )
        }

    }

}

export default Search;