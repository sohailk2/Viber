
import React from 'react';
import { Box, Layer, DropButton, Main, Heading, Form, FormField, TextInput } from 'grommet';
import Star from './Star.js'

export default function SongComponent(props) {
    return (
        <>
        <DropButton hoverIndicator={true} onClick={() => {props.onClick(props.song.id)}}
            dropAlign={{bottom: 'bottom', left: 'right', right: 'right' }}
            dropContent={props.dropContent}
        >
            <Box margin="small" pad="small" background="light-3">
                <h2>{props.song.title}</h2>
                

                <Box direction="row">
                    <Box pad={{ right: "55px" }}>{props.song.artist_name} - {props.song.popularity}</Box>
                </Box>
               
            </Box>

        </DropButton>
        
        </>
    )
}