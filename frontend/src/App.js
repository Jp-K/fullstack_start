import {resp, post, delet} from "./req"
import {useState} from "react"


function App() {

  const func = async () => {
    const response = await resp();
    setResponse(response.data);
    console.log(response);
  }

  const func2 = async () => {
    const response = await post(["1", "2"]);
  }

  const func3 = async () => {
    const response = await delet();
  }
  
  const [response, setResponse] = useState({});

  return (
    <div className="block">
      <div>
      <button onClick={func} className=" border-rounded bg-green-600">ler</button>
      </div>
      <div>
      <button onClick={func2} className=" border-rounded bg-green-600">escrever</button>
      </div>
      <div>
      <button onClick={func3} className="border-rounded bg-green-600">remover/editar</button>
      </div>
      <div></div>
      <h1>{response.email}</h1>
    </div>
  );
}

export default App;
