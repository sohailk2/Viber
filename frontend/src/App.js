import logo from './logo.svg';
import './App.css';
import Home from './components/Home.js'
import { Button, Grommet, Text, Nav, Anchor, Header, Menu } from 'grommet';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect,
  withRouter
} from "react-router-dom";

import Login from './components/Login';
import React from 'react';
import { SpotifyApiContext } from 'react-spotify-api';
import { User, Artist } from 'react-spotify-api'
import axios from 'axios';

import Search from './components/Search.js'
import Results from './components/Results.js'
import UserInfo from './components/UserInfo.js'

class App extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      token: null,
      redirect: null,
      userInfo: null
      // token: "BQCb9BsaeFRV9oyCLAtROzMWebIgLvA5pOcHblqShF6gaVLPEXWvjkoF0H-IXb1KXczz10MgcptLYiHnfrkymDw9xOc_ACB3jvZi24cK0zxIGmVIRGdImH__Tv0owrGOk3h_l2l9kf6PpqBStTS9ic3SIdNL-Js8"
    };

  }

  updateUserToken = (user_token) => {
    this.setState({ token: user_token });
  }

  updateUserInfo = (userInfo) => {
    this.setState({ userInfo: userInfo });
  };

  render() {


    return (
      <SpotifyApiContext.Provider value={this.state.token}>

        {/* <Nav direction="row" background="brand" pad="medium">
          <Anchor onClick={() => { this.setState({ redirect: '/search' }) }} label="Search" />
          <Anchor href="#" label="For Example" />
        </Nav> */}


        <Grommet theme={{ global: { colors: { doc: '#ff99cc' } } }}
        >

          <Router>

            <Header background="brand">
              <Nav direction="row" background="brand" pad="medium">
                <Link to="/userinfo" style={{ textDecoration: 'none' }}>
                  <Anchor label="User Info" />
                </Link>

                <Link to="/search" style={{ textDecoration: 'none' }}>
                  <Anchor label="Search" />
                </Link>

              </Nav>
            </Header>

            <div style={{
              position: 'absolute', left: '50%', top: '60%',
              transform: 'translate(-50%, -50%)'
            }}>


              <Switch>

                <Route path="/callback">
                  <Login updateUserToken={this.updateUserToken} />
                </Route>

                {this.state.token == null ?
                  <Home /> :
                  <>
                    <Route path="/userinfo">


                      {/* <UserInfo token={this.state.tempToken} /> */}
                      <UserInfo updateUserInfo={this.updateUserInfo} token={this.state.token} userInfo={this.state.userInfo} />

                      {/* <Link to="/search">
                      <Button primary label="Search" />
                    </Link> */}


                    </Route>

                    <Route path="/search">
                      <Search userInfo={this.state.userInfo} />
                    </Route>


                    <Route path="/playlist/:songID"
                      // children={<Results songID = {params.match.songID} userInfo = {this.state.userInfo}/>}   
                      render={(props) => <Results userInfo = {this.state.userInfo} {...props} /> }
                    />
                  </>
                }
              </Switch>
            </div>
          </Router>

        </Grommet>
      </SpotifyApiContext.Provider >

    );
  }

}


export default App;
