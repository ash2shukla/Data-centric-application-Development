import React, { ReactNode } from "react"
import {
  withStreamlitConnection,
  StreamlitComponentBase,
  Streamlit,
} from "./streamlit"

interface State {
  watchId: number,
  enableHighAccuracy: boolean,
  timeout: number,
  maximumAge: number
}

class StreamlitLocationComponent extends StreamlitComponentBase<State> {
  public state = { watchId: -1, enableHighAccuracy: false, timeout: 36_00_000, maximumAge: 0 }
  private methodMap = new Map<String, Function>(
    [
      ["location", this.location],
      ["watch", this.watch],
    ]
  )

  private location() {
    navigator.geolocation.getCurrentPosition(
      point => {
        const result = {
          latitude: point.coords.latitude,
          longitude: point.coords.longitude,
          accuracy: point.coords.accuracy,
          speed: point.coords.speed,
          altitude: point.coords.altitude,
          altitudeAccuracy: point.coords.altitudeAccuracy
        }
        Streamlit.setComponentValue(result);
      }
    )
  }

  private watch() {
    const opts = {
      enableHighAccuracy: this.state.enableHighAccuracy,
      timeout: this.state.timeout,
      maximumAge: this.state.maximumAge
    }
    const id = navigator.geolocation.watchPosition(
      point => {
        const result = {
          latitude: point.coords.latitude,
          longitude: point.coords.longitude,
          accuracy: point.coords.accuracy,
          speed: point.coords.speed,
          altitude: point.coords.altitude,
          altitudeAccuracy: point.coords.altitudeAccuracy,
          err: null
        }
        Streamlit.setComponentValue(result);
      },
      err => {
        const result = {
          latitude: null,
          longitude: null,
          accuracy: null,
          speed: null,
          altitude: null,
          altitudeAccuracy: null,
          error: err,
        }
        Streamlit.setComponentValue(result)
      },
      opts
    )
    this.setState({ watchId: id })
  }

  componentDidMount() {
    const methodName = this.props.args["method_intent"]
    const method = this.methodMap.get(methodName)
    if (method !== undefined) {
      method.bind(this)();
    }
    Streamlit.setFrameHeight(100);
  }

  componentWillUnmount() {
    navigator.geolocation.clearWatch(this.state.watchId);
  }

  public render = (): ReactNode => {
    return <span></span>
  }
}

export default withStreamlitConnection(StreamlitLocationComponent)
