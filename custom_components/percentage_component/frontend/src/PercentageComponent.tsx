import {
  Streamlit,
  withStreamlitConnection,
  ComponentProps,
} from "streamlit-component-lib"
import React, { useEffect, ReactElement, useState } from "react"

function PercentageComponent({ args }: ComponentProps): ReactElement {
  const { percentage } = args
  const [currentPercentage, setCurrentPercentage] = useState(0);

  useEffect(() => {
    Streamlit.setFrameHeight();

    // Calculate the difference and the number of steps
    const difference = percentage - currentPercentage;
    const steps = Math.abs(difference);
    const stepSize = difference === 0 ? 0 : difference / steps; // Calculate step size
    const milisecondsToCompletion = 300;
    const intervalDuration = milisecondsToCompletion / steps;

    const interval = setInterval(() => {
      setCurrentPercentage(prev => {
        if (prev < percentage) {
          return Math.min(prev + stepSize, percentage); 
        } else if (prev > percentage) {
          return Math.max(prev + stepSize, percentage); 
        } else {
          clearInterval(interval);
          return prev;
        }
      });
    }, intervalDuration); 

    return () => clearInterval(interval); // Cleanup on unmount
  }, [percentage]);

  const getColor = (percentage: number) => {
    if (percentage < 50) {
      return '#e74c3c'; // red
    }
    if (percentage < 70) {
      return '#f39c12'; // orange
    } 
    return '#2ecc71'; // green
  };

  const color = getColor(currentPercentage);

  return (
    <div style={{
      textAlign: "center",
      padding: "10px",
      border: `2px solid ${color}`,
      borderRadius: "10px",
      width: "100%",
      background: `linear-gradient(to right, ${color} ${currentPercentage}%, transparent ${currentPercentage}%)`, // Gradient background
    }}>
      <span style={{ fontSize: "24px", fontWeight: "bold" }}>
        {currentPercentage.toFixed(1)}%
      </span>
    </div>
  )
}

export default withStreamlitConnection(PercentageComponent)
