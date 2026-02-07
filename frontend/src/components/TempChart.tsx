import React from 'react';
interface Props { sensorId: number; }
export default function TempChart({ sensorId }: Props) {
  return <div id={`chart-${sensorId}`}>Temperature Chart Placeholder</div>;
}
