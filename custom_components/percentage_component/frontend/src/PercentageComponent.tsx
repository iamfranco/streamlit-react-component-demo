import {
  Streamlit,
  withStreamlitConnection,
  ComponentProps,
} from "streamlit-component-lib"
import React, { useEffect, ReactElement } from "react"

function PercentageComponent({ args }: ComponentProps): ReactElement {
  const { percentage } = args
  useEffect(() => {
    Streamlit.setFrameHeight()
  }, [])

  const getColor = (percentage: number) => {
    if (percentage < 50) {
      return '#e74c3c'; // red
    }
    if (percentage < 70) {
      return '#f39c12'; // orange
    } 
    return '#2ecc71'; // green
  };

  let color = getColor(percentage);

  return (
    <div style={{
      textAlign: "center",
      padding: "10px",
      border: `2px solid ${color}`,
      borderRadius: "10px",
      width: "100%",
      background: `linear-gradient(to right, ${color} ${percentage}%, #ffffff ${percentage}%)`, // Gradient background
    }}>
      <span style={{ fontSize: "24px", fontWeight: "bold" }}>
        {percentage}%
      </span>
    </div>
  )
}

export default withStreamlitConnection(PercentageComponent)
