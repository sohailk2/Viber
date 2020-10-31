import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Text, Grid, Box, Button, InfiniteScroll, Form, FormField, TextInput } from 'grommet';
import { useHistory } from "react-router-dom";


import SongComponent from './SongComponent';

export default function UserInfo(props) {

    let history = useHistory();
    const [page, setPage] = useState(1);
    const [userInfo, setUserInfo] = useState(null);
    // history.push('/someRoute')


    // const token = "BQAD4pJHqlvDpcne93XTG7S1rr09ik0H7unN8aH7bTBdpr-berpK_om4qW1JhLTullh-miTq8zrruznHFW4dviMyHyg79wig4ImJs0Vbxi-rOxsj-POxSZ_A_rTz6_AXf_e92dcP95n8o5ExBpNGaqGl5cGWrx6l"
    const token = props.token;

    useEffect(() => {
        const config = {
            headers: { Authorization: `Bearer ${token}` }
        };


        axios.get(`https://api.spotify.com/v1/me`, config)
            .then(res => {
                console.log(res);
                console.log(res.data);
                setUserInfo(res.data);

            })
    }, [page]);

    return (
        <div style={{ width: '100%' }}>
            {userInfo ?

                <div>
                    <h1>Hello <Text color="brand">{userInfo.display_name}</Text></h1>
                    {/* {JSON.stringify(userInfo)} */}

                    <Box
                        direction="row"
                        // border={{ color: 'brand', size: 'large' }}
                        pad="medium"
                    >
                        <Box style={{ height: '500px', width: '80%' }} overflow="scroll" margin="large" pad="medium" background="dark-3">
                            <div>
                                <h2>Previous Searches</h2>
                                <PreviousSearches userID="1" />
                            </div>
                        </Box>

                        <Box overflow="scroll" style={{ height: '500px', width: '80%' }} margin="large" pad="medium" background="dark-3">
                            <div>
                                <h2>Friends</h2>
                                <Box margin="small" pad="small" background="light-3">
                                    <AddFriend />
                                </Box>

                                <Box overflow="scroll">
                                    <DisplayFriends userID="1" />
                                </Box>
                            </div>
                        </Box>
                    </Box>

                </div>

                : 'NO USER YET'}

            {/* {token} */}
        </div>


    )
}

function PreviousSearches(props) {

    const [searches, setSearches] = useState(null);

    useEffect(() => {
        axios.get(`http://127.0.0.1:8000/viber/getSearches/${props.userID}/`)
            .then(res => {
                console.log(res.data);
                setSearches(res.data.data)
            })
    }, []);

    if (searches == null) {
        return ("LOADING...")
    } else {
        return (

            <Box>
                {searches.map((song, index) => (<SongComponent key={song.id} song={song} onClick={() => { }} />))}
            </Box>
        )
    }

}

function DisplayFriends(props) {
    const [friends, setFriends] = useState(null);

    useEffect(() => {
        axios.get(`http://127.0.0.1:8000/viber/getFriends/${props.userID}/`)
            .then(res => {
                console.log(res.data);
                setFriends(res.data.data)
            })
    }, []);

    if (friends == null) {
        return ("LOADING...")
    } else {
        return (
            friends.map((friend, index) => (<Friend key={friend.id} friend={friend} />))
        )
    }
}

function Friend(props) {
    return (
        <Box margin="small" pad="small" background="light-3">
            <h3>{props.friend.name}</h3>
            <Button hoverIndicator={true} color="status-error" label="Delete" />
            {/* <Box direction="row">
                <Box pad={{ right: "55px" }}>idk other info???</Box>
            </Box> */}

        </Box>
    )
}

function AddFriend() {
    {/* <h3>Enter UserID</h3>
                                    
                                    <Button hoverIndicator={true} color="status-ok" label="Add Friend" /> */}

    const [value, setValue] = React.useState({});
    return (
        <Form
            value={value}
            onChange={nextValue => setValue(nextValue)}
            onReset={() => setValue({})}
            onSubmit={({ value }) => { }}
        >
            <FormField name="username" htmlfor="text-input-id" label="Username">
                <TextInput id="text-input-id" name="username" />
            </FormField>

            <Button type="submit" color="status-ok" label="Add Friend" />
        </Form>
    );
}