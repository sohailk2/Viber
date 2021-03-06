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
            formData: {},
            playlist: null,
            songSelected: null,
            errors: {},
        };
    }

    componentDidMount() {
        // this.getData("song name");
    }

    validate = () => {

        //as long as smthn is put in the 
        let valid = 0;

        if(this.state.formData.hasOwnProperty('songName') && !this.state.formData.songName.trim() == ""){
            // this.setState({errors:{"songName": "Enter a name"}});
            // return false;
            valid++;
        }

        if(this.state.formData.hasOwnProperty('artistName') && !this.state.formData.artistName.trim() == ""){
            valid++;
        }

        return valid;
    }

    submitForm = () => {
        if (this.validate()) {
            // alert(JSON.stringify(this.state.formData))
            this.getData(this.state.formData);
        }
    };


    getData = (query) => {
        // var csrftoken = Cookies.get('csrftoken');
        axios.post(`http://127.0.0.1:8000/viber/search/`, query,
        )
        .then(res => {
            console.log("DATA", res.data.data);
            this.setState({playlist : res.data.data})
        });
    }

    getPlaylist = (songID) => {

        //custom callbacks hack so dont have to rewrite the whole thing
        if (this.props.customCallBack) {
            this.props.customCallBack(songID);
        } else {
            //default behavior to go to similar screen
            // alert(songID);
            this.setState({songSelected: songID});
        }

        
    }

    render() {

        if (this.state.songSelected)  {
            return <Redirect to={"/playlist/" + this.state.songSelected} />
        }

        if (this.state.playlist == null) {
            return (


                <Form
                    value={this.state.formData}
                    onChange={nextValue => this.setState({ formData: nextValue })}
                    onReset={() => this.setState({ formData : {} })}
                    onSubmit={this.submitForm}
                    errors={this.state.errors}
                >
                    <FormField name="songName" htmlfor="text-input-id" label="Enter a song name!">
                        <TextInput id="text-input-id" name="songName" />
                    </FormField>

                    <FormField name="artistName" htmlfor="text-input-id" label="Enter an artist name!">
                        <TextInput id="text-input-id-2" name="artistName" />
                    </FormField>

                    <Box direction="row" gap="medium">
                        <Button type="submit" primary label="Submit" onClick={() => this.submitForm()} />
                        <Button type="reset" label="Reset"/>
                    </Box>

                </Form>

            );
        } else {

            // display the pklaylist
            return (

                <div>
                    <Heading>Search Results:</Heading>
                    <Box
                        overflow="scroll"
                        direction="column"
                        border={{ color: 'brand', size: 'large' }}
                        pad="small"
                        style={{ width: "500px", height: '500px' }}
                    >
                        {this.state.playlist.map((song, index) => (<SongComponent key={song.track_id} song={song} onClick={() => {this.getPlaylist(song.track_id)}}/>))}
                    </Box>
                    
                    <Button margin="large" type="reset" label="Reset" onClick={() => {this.setState({ playlist: null });this.setState({ formData : {} })}} />
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