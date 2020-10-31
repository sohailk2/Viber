import React from 'react';
import { Box, Layer, Button, Main, Heading, Form, FormField, TextInput } from 'grommet';
import axios from 'axios';
import Cookies from 'js-cookie';
import { Redirect } from "react-router-dom";
import SongComponent from './SongComponent'

class Search extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            formData: "",
            playlist: null,
            songSelected: null
        };
    }

    componentDidMount() {
        this.getData("song name");
    }

    submitForm = () => {
        this.getData("other");
    };

    getData = (query) => {
        // var csrftoken = Cookies.get('csrftoken');
        axios.post(`http://127.0.0.1:8000/viber/search/`,
        {
            songName: query
        },
        )
        .then(res => {
            // console.log("DATA", res.data.data);
            this.setState({playlist : res.data.data})
        });
    }

    getPlaylist = (songID) => {
        // alert(songID);
        this.setState({songSelected: songID});
    }

    render() {

        if (this.state.songSelected)  {
            return <Redirect to={"/playlist/" + this.state.songSelected} />
        }

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
                        {this.state.playlist.map((song, index) => (<SongComponent key={song.id} song={song} onClick={this.getPlaylist}/>))}
                    </Box>
                    <Button margin="large" type="reset" label="Reset" onClick={() => this.setState({ playlist: null })} />
                </div>

            )
        }

    }

}


// function SongComponent(props) {
//     return (
//         <Button hoverIndicator={true} onClick={() => {props.getPlaylist(props.song.id)}}>
//             <Box margin="small" pad="small" background="light-3">
//                 <h2>{props.song.name}</h2>

//                 <Box direction="row">
//                     <Box pad={{ right: "55px" }}>{props.song.artist}</Box>
//                 </Box>
                
//             </Box>
//         </Button>
//     )
// }

export default Search;