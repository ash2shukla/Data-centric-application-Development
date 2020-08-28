// CHANGE HERE: this file'name name to ComponentNameComponent.tsx

import React, { ReactNode } from "react"
import {
  withStreamlitConnection,
  StreamlitComponentBase,
  Streamlit,
} from "./streamlit"

// add stateful thing's interface
interface State {}

// CHANGE HERE: with component class name
class StreamlitComponent extends StreamlitComponentBase<State> {
  // initialize stateful things
  public state = { }

  componentDidMount() {
   // create necessary stuff
   // get arguments passed by python here likt this.
   this.props.args["python_argument"]

   Streamlit.setComponentValue("Pass the return value to Python side from here")
  }

  componentWillUnmount() {
    // remove unnecessary stuff
  }

  public render = (): ReactNode => {
    return <div>Test.</div>
  }
}

// CHANGE HERE: with component class name
export default withStreamlitConnection(StreamlitComponent)
