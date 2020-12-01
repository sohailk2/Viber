
import React, { useState, useEffect } from 'react';
import { Box, Layer, DropButton, Main, Heading, Form, FormField, TextInput } from 'grommet';
import axios from 'axios';

export default function SongComponent(props) {

    const [awards, setAwards] = useState([]);

    useEffect(() => {
        // console.log(props);
        axios.get(`http://127.0.0.1:8000/viber/getSongAwards/${props.song.track_id}/`)
            .then(res => {
                console.log("SONG COMP: ", res.data);
                // alert(res.data);
                setAwards(Object.keys(res.data));
            })
    }, [props.song.track_id]);

    let viewPlaylist = (songID) => {
        props.history.push({ pathname: `/playlist/${songID}` });
    }

    return (
        <>
        <DropButton hoverIndicator={true} onClick={() => {props.onClick(props.song.id)}}
            dropAlign={props.dropAlign}
            dropContent={props.dropContent}
        >
            <Box margin="small" pad="small" background="light-3">
                <h2>{props.song.title}</h2>
                

                <Box direction="row">
                    <Box pad={{ right: "55px" }}>{props.song.artist_name} - {awards.map((award) =><li>{award}</li>)}</Box>
                </Box>
               
            </Box>

        </DropButton>
        
        </> 
    )
}