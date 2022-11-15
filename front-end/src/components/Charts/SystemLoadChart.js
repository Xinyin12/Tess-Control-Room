import React from "react";
import axios from "axios";
import {QueryClient, QueryClientProvider, useQuery} from "react-query";
import {Line} from "react-chartjs-2";
import {systemLoadChartOption} from "../../variables/chartOptions";

function SystemLoadChart(props) {
    return (
        <QueryClientProvider client={new QueryClient()}>
            <SystemLoadChartCore/>
        </QueryClientProvider>
    );
}


function SystemLoadChartCore(props) {
    const dataFetchFunc = async () => {
        const { data } = await axios.get(
            'https://dummyjson.com/carts'
        );
        return data;
    };

    const time = [];
    const actualCapacity = [];
    const clearedCapacity = [2000, 3050, 4874, 1643, 2984, 5237, 7720, 3205, 8237, 2332, 4038];
    const {
        isLoading,
        isSuccess,
        error,
        isError,
        data: systemLoadData
    } = useQuery("systemLoad", dataFetchFunc, {refetchInterval: 300000});
    if (isSuccess) {
        for (let i = 0; i < systemLoadData.carts.length; i++) {
            time[i] = systemLoadData.carts[i].id;
            actualCapacity[i] = systemLoadData.carts[i].total;
        }
    }

    let systemLoadChart = {
        data: (canvas) => {
            let ctx = canvas.getContext("2d");

            let gradientStroke = ctx.createLinearGradient(0, 230, 0, 50);

            gradientStroke.addColorStop(1, "rgba(29,140,248,0.2)");
            gradientStroke.addColorStop(0.4, "rgba(29,140,248,0.0)");
            gradientStroke.addColorStop(0, "rgba(29,140,248,0)"); //blue colors

            return {
                labels: time,
                datasets: [
                    {
                        label: "Actual",
                        fill: false,
                        backgroundColor: gradientStroke,
                        borderColor: "#1f8ef1",
                        borderWidth: 2,
                        borderDash: [],
                        borderDashOffset: 0.0,
                        pointBackgroundColor: "#1f8ef1",
                        pointBorderColor: "rgba(255,255,255,0)",
                        pointHoverBackgroundColor: "#1f8ef1",
                        pointBorderWidth: 20,
                        pointHoverRadius: 4,
                        pointHoverBorderWidth: 15,
                        pointRadius: 4,
                        data: actualCapacity
                    },
                    {
                        label: "Cleared",
                        fill: false,
                        backgroundColor: gradientStroke,
                        borderColor: "#f11fce",
                        borderWidth: 2,
                        borderDash: [],
                        borderDashOffset: 0.0,
                        pointBackgroundColor: "#f11fce",
                        pointBorderColor: "rgba(241,31,206,0)",
                        pointHoverBackgroundColor: "#f11fce",
                        pointBorderWidth: 20,
                        pointHoverRadius: 4,
                        pointHoverBorderWidth: 15,
                        pointRadius: 4,
                        data: clearedCapacity
                    }
                ]
            };
        },
        options: systemLoadChartOption
    };

    return (
        <Line
            data={systemLoadChart.data}
            options={systemLoadChart.options}
        />
    );
}

export default SystemLoadChart;
