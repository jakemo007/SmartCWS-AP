import ReactApexChart from 'react-apexcharts';

export function BarChart({ data }) {
  const options = {
    chart: { type: 'bar' },
    xaxis: { categories: data.labels },
    colors: ['#4F46E5'],
  };
  return <ReactApexChart options={options} series={[{ data: data.values }]} type="bar" height={300} />;
}

export function PieChart({ data }) {
  const options = {
    labels: data.labels,
    colors: ['#4F46E5', '#6366F1', '#A5B4FC'],
  };
  return <ReactApexChart options={options} series={data.values} type="pie" height={300} />;
}