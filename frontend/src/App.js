import logo from './logo.svg';
import './App.css';
import Home from './components/Home.js'
import { Grommet } from 'grommet';

function App() {
  return (
    <Grommet 
      theme={{ global: { colors: { doc: '#ff99cc' } } }}
      style={{
        position: 'absolute', left: '50%', top: '50%',
        transform: 'translate(-50%, -50%)'}}>
        <Home/>
    </Grommet>
    
  );
}

export default App;
