import logo from './logo.svg';
import './App.css';
import Home from './components/Home.js'
import { Button, Grommet, Text } from 'grommet';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import Login from './components/Login';
import React, { useState, useEffect } from 'react';
import { SpotifyApiContext } from 'react-spotify-api';
import { User, Artist } from 'react-spotify-api'
import axios from 'axios';

import Search from './components/Search.js'
import Results from './components/Results.js'


class App extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      token: null,
      // token: "BQCb9BsaeFRV9oyCLAtROzMWebIgLvA5pOcHblqShF6gaVLPEXWvjkoF0H-IXb1KXczz10MgcptLYiHnfrkymDw9xOc_ACB3jvZi24cK0zxIGmVIRGdImH__Tv0owrGOk3h_l2l9kf6PpqBStTS9ic3SIdNL-Js8"
    };

  }

  updateUser = (user_token) => {
    this.setState({ token: user_token });
  }

  render() {
    return (
        <SpotifyApiContext.Provider value={this.state.token}>
        <Grommet theme={{ global: { colors: { doc: '#ff99cc' } } }}
          style={{
            position: 'absolute', left: '50%', top: '50%',
            transform: 'translate(-50%, -50%)'
          }}>

          <Router>
            <Switch>

              <Route path="/a">
                hi
            </Route>

              <Route path="/callback">
                <Login updateUser={this.updateUser} />
              </Route>

              <Route path="/page1">
                {/* <UserInfo token={this.state.tempToken} /> */}
                <UserInfo token={this.state.token} />

                <Link to="/search">
                  <Button primary label="Search"/>
                </Link>

              </Route>

              <Route path="/search">
                <Search/>
              </Route>

              <Route path="/playlist/:id" component={Results}/>
                
              <Route path="/">
                <Home />
              </Route>

            </Switch>


          </Router>

        </Grommet>
      </SpotifyApiContext.Provider>

    );
  }

}

function UserInfo(props) {



  // return (

  // <Artist id="1XpDYCrUJnvCo9Ez6yeMWh">
  //   {({ data, loading, error }) =>
  //     data ? (
  //       <div>
  //         <h1>{data.name}</h1>
  //         <ul>
  //           {data.genres.map(genre => (
  //             <li key={genre}>{genre}</li>
  //           ))}
  //         </ul>
  //       </div>
  //     ) : null
  //   }
  // </Artist>
  // )

  const [page, setPage] = useState(1);
  const [userInfo, setUserInfo] = useState(null);

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
    <p> {userInfo ?

      <div>
        <h1>Hello <Text color="brand">{userInfo.display_name}</Text></h1>
        {JSON.stringify(userInfo)}
        <br></br>

      </div>

      : 'NO USER YET'}

      {token}
    </p>


  )
}

export default App;
