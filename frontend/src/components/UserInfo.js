import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Text, Grid, Box, Button, Anchor, Form, FormField, TextInput } from 'grommet';
import { useHistory } from "react-router-dom";


import SongComponent from './SongComponent';

export default function UserInfo(props) {

    let history = useHistory();
    const [page, setPage] = useState(1);
    // const [props.userInfo, setUserInfo] = useState(null);
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
                // setUserInfo(res.data);
                props.updateUserInfo(res.data);
            })
    }, [page]);

    return (
        <div style={{ width: '100%' }}>
            {props.userInfo ?

                <div>
                    <h1>Hello <Anchor target="_blank" href={props.userInfo.external_urls.spotify}><Text size="xlarge" color="brand">{props.userInfo.display_name}</Text></Anchor></h1>
                    {/* {JSON.stringify(userInfo)} */}

                    <Box
                        direction="row"
                        // border={{ color: 'brand', size: 'large' }}
                        pad="medium"
                    >
                        <Box style={{ height: '500px', width: '80%' }} overflow="scroll" margin="large" pad="medium" background="dark-3">
                            <div>
                                <h2>Previous Searches</h2>
                                <PreviousSearches userInfo={props.userInfo} history={history}/>
                            </div>
                        </Box>

                        <Box overflow="scroll" style={{ height: '500px', width: '80%' }} margin="large" pad="medium" background="dark-3">
                            <div>
                                <h2>Friends</h2>
                                <Box margin="small" pad="small" background="light-3">
                                    <AddFriend userInfo={props.userInfo} history={history}/>
                                </Box>

                                <Box overflow="scroll">
                                    <DisplayFriends userInfo={props.userInfo} history={history}/>
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
        axios.get(`http://127.0.0.1:8000/viber/getSearches/${props.userInfo.display_name}/`)
            .then(res => {
                console.log(res.data);
                setSearches(res.data.data)
            })
    }, []);

    let viewPlaylist = (songID) => {
        props.history.push({ pathname: `/playlist/${songID}` });
    }
    
    if (searches == null) {
        return ("LOADING...")
    } else {
        return (

            <Box>
                {searches.map((song, index) => (<SongComponent key={song.track_id} song={song} onClick={() => viewPlaylist(song.track_id)}/>))}
            </Box>
        )
    }

}

function DisplayFriends(props) {
    const [friends, setFriends] = useState(null);

    useEffect(() => {
        axios.get(`http://127.0.0.1:8000/viber/getFriends/${props.userInfo.display_name}/`)
            .then(res => {
                console.log(res.data);
                setFriends(res.data.data)
            })
    }, []);

    if (friends == null) {
        return ("LOADING...")
    } else {
        return (
            friends.map((friend, index) => (<Friend key={friend.display_name} currUser={props.userInfo} friend={friend} history={props.history}/>))
        )
    }
}

function Friend(props) {

    const [confirmDelete, setConfirmDelete] = useState(false);

    let deleteFriend = () => {
        axios.post(`http://127.0.0.1:8000/viber/delFriend/`, {currUser: props.currUser.display_name, friend: props.friend.display_name})
        .then(res => {
            props.history.push({ pathname: "/empty" });
            props.history.replace({ pathname: "/userinfo" });
        }) 

    }

    return (
        <Box margin="small" pad="small" background="light-3">
            <h3>{props.friend.display_name}</h3>
            
            {confirmDelete ? 
                <span>Confirm Delete<Button hoverIndicator={true} color="status-error" label="Yes" onClick={() => {deleteFriend()}}/></span>
                :
                <Button hoverIndicator={true} color="status-error" label="Delete" onClick={() => {setConfirmDelete(true)}}/>
            }


        </Box>
    )
}

function AddFriend(props) {

    const [value, setValue] = React.useState({});
    const [errors, setErrors] = React.useState({});


    let addFriendCall = () => {
        
        if (validate()) {
            axios.post(`http://127.0.0.1:8000/viber/addFriend/`, {currUser: props.userInfo.display_name, friend: value.username})
            .then(res => {
                props.history.push({ pathname: "/empty" });
                props.history.replace({ pathname: "/userinfo" });
            }) 
        }
        
    }

    let validate = () => {

        if(!value.hasOwnProperty('username') || value.username.trim() == ""){
            setErrors({"username": "Enter a name"});
            return false;
        }

        return true;
        
    }

    return (
        <Form
            value={value}
            onChange={nextValue => setValue(nextValue)}
            onReset={() => setValue({})}
            onSubmit={addFriendCall}
            errors={errors}
            // onValidate={validate}
        >
            <FormField name="username" htmlfor="text-input-id" label="Username">
                <TextInput id="text-input-id" name="username" />
            </FormField>

            <Button type="submit" color="status-ok" label="Add Friend" />
        </Form>
    );
}