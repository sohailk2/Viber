import logo from './logo.svg';
import './App.css';
import Home from './components/Home.js'
import { Grommet } from 'grommet';
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



class App extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      token: null,
    };

  }

  updateUser = (user_token) => {
    this.setState({ token: user_token });
  }

  render() {
    return (
      <SpotifyApiContext.Provider value={"BQAD4pJHqlvDpcne93XTG7S1rr09ik0H7unN8aH7bTBdpr-berpK_om4qW1JhLTullh-miTq8zrruznHFW4dviMyHyg79wig4ImJs0Vbxi-rOxsj-POxSZ_A_rTz6_AXf_e92dcP95n8o5ExBpNGaqGl5cGWrx6l"}>
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
                <UserInfo token={this.state.token} />
              </Route>

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
  const [userName, setUserName] = useState();

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
      setUserName(JSON.stringify(res.data));

    })
  }, [page]);

  return (
    <p> {token ? "user:" + userName : 'NO USER YET'}</p>
  )
}

export default App;
