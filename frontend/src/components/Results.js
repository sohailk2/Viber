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
                console.log("DATA", res.data.data);
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
                return ("NO RESULTS")
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
                                <SongComponent key={this.state.currSong.id} song={this.state.currSong} onClick={() => {}} />


                            </Main>
                        </Box>
                        <Box
                            overflow="scroll"
                            direction="column"
                            border={{ color: 'brand', size: 'large' }}
                            pad="small"
                            style={{ width: "500px", height: '500px' }}
                        >
                            {this.state.playlist.map((song, index) => (<SongComponent key={song.id} song={song} dropContent={<SimilarityMetric/>} onClick={() => { }} />))}
                        </Box>
                    </Box>
                )
            }
        }

    }

}

function SimilarityMetric(props) {
    return (
        <Box margin="large">
            <Main>Similarity Metrics</Main>
            <Chart
            bounds={[[0, 7], [0, 100]]}
            animate
            values={[
                { value: [7, 100], label: 'one hundred' },
                { value: [6, 70], label: 'seventy' },
                { value: [5, 60], label: 'sixty' },
                { value: [4, 80], label: 'eighty' },
                { value: [3, 40], label: 'forty' },
                { value: [2, 0], label: 'zero' },
                { value: [1, 30], label: 'thirty' },
                { value: [0, 60], label: 'sixty' },
            ]}
            aria-label="chart"
        />
        </Box>
    )
}

export default Results;