import React from 'react';
import { Box, Main, Heading, Chart} from 'grommet';
import { useParams } from "react-router-dom";
import axios from 'axios';
import SongComponent from './SongComponent'


class Results extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            playlist: null,
            error: null,
            currSong: null
        };

    }

    componentDidMount() {
        // TRKTVOR128F4217228
        const songID = this.props.match.params.songID;

        //get the playlist
        this.getData(songID);

        //gets the card for the original song
        this.getSongInfo(songID);

    }

    getData = (songID) => {
        // console.log(this.props.userInfo.display_name);
        // var csrftoken = Cookies.get('csrftoken');
        axios.post(`http://127.0.0.1:8000/viber/getPlaylist/`, {
            "track_id" : songID,
            "UID" : this.props.userInfo.display_name
        })
            .then(res => {
                // console.log("DATA", res.data.data);
                this.setState({ playlist: res.data.data, error: res.data.error })
            });
    }

    getSongInfo = (songID) => {
        axios.get(`http://127.0.0.1:8000/viber/getSong/${songID}/`)
            .then(res => {
                this.setState({ currSong: res.data })
            });
    }

    render() {
        if (this.state.error != null) {
            return (
                "ERROR"
            )
        } else {
            if (this.state.playlist == null || this.state.playlist.length == 0 || this.state.currSong == null) {
                return ("Loading...")
            } else {
                return (
                    <Box direction="row">
                        <Box>
                            <Main pad="large">
                                <span>
                                    <Heading>
                                        Results for: 
                                    </Heading>
                                </span>

                                {/* REMEBER TO RESTORE BACK TO ORIGINAL */}
                                {/* <SongComponent key={this.state.currSong.id} song={this.state.currSong} onClick={() => {this.getData(this.props.match.params.songID)}} /> */}
                                <SongComponent key={this.state.currSong.id} song={this.state.currSong} dropAlign={{ bottom: 'top', right: 'right' }} dropContent={<SimilarityMetric song={this.state.currSong}/>} onClick={() => {this.getData(this.props.match.params.songID)}} />


                            </Main>
                        </Box>
                        <Box
                            overflow="scroll"
                            direction="column"
                            border={{ color: 'brand', size: 'large' }}
                            pad="small"
                            style={{ width: "500px", height: '500px' }}
                        >
                            {this.state.playlist.map((song, index) => (<SongComponent key={song.id} song={song} dropAlign={{bottom: 'bottom', left: 'right', right: 'right' }} dropContent={<SimilarityMetric song={song}/>} onClick={() => { }} />))}
                        </Box>
                    </Box>
                )
            }
        }

    }

}

function SimilarityMetric(props) {
    console.log("SONG INFO:", props.song);
    // alert("SONG INFO:", props.song);
    return (
        <Box margin="large">
            <Main>Similarity Metrics</Main>
            <Chart
            bounds={[[0, 4], [0, 1]]}
            animate
            // values={[
            //     { value: [6, props.song.valence], label: 'valence' },
            //     { value: [5, props.song.instrumentalness], label: 'instrumentalness' },
            //     { value: [4, props.song.acousticness], label: 'acousticness' },
            //     { value: [3, props.song.speechiness], label: 'speechiness' },
            //     // { value: [2, props.song.loudness], label: 'loudness' },
            //     { value: [1, props.song.energy], label: 'energy' },
            //     { value: [0, props.song.danceability], label: 'danceability' },
            // ]}
            values={[
                { value: [4, props.song.valence], label: 'valence' },
                // { value: [4, props.song.instrumentalness * 10], label: 'instrumentalness' },
                { value: [3, props.song.acousticness], label: 'acousticness' },
                { value: [2, props.song.speechiness], label: 'speechiness' },
                // { value: [2, props.song.loudness], label: 'loudness' },
                { value: [1, props.song.energy], label: 'energy' },
                { value: [0, props.song.danceability], label: 'danceability' },
            ]}
            aria-label="chart"
        />
        </Box>
    )
}

export default Results;