// src/components/Charts.js
import React from 'react';
import ReactApexChart from 'react-apexcharts';

export const BarChart = ({ data }) => {
  const options = {
    chart: { type: 'bar', toolbar: { show: false } },
    plotOptions: { bar: { borderRadius: 4, horizontal: false } },
    dataLabels: { enabled: false },
    xaxis: { categories: data?.labels || [], title: { text: data?.xAxisTitle || '' } },
    yaxis: { title: { text: data?.yAxisTitle || '' } },
    colors: ['#4F46E5']
  };

  return (
    <ReactApexChart
      options={options}
      series={[{ name: data?.seriesName || 'Data', data: data?.values || [] }]}
      type="bar"
      height={350}
    />
  );
};

export const PieChart = ({ data }) => {
  const options = {
    labels: data?.labels || [],
    colors: ['#4F46E5', '#6366F1', '#A5B4FC'],
    legend: { position: 'right' }
  };

  return (
    <ReactApexChart
      options={options}
      series={data?.values || []}
      type="pie"
      height={350}
    />
  );
};

export default { BarChart, PieChart };