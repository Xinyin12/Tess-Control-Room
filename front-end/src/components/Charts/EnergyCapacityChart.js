import React from "react";
import axios from "axios";
import {QueryClient, QueryClientProvider, useQuery} from "react-query";
import {Line} from "react-chartjs-2";
import {energyCapacityChartOption} from "../../variables/chartOptions";

function EnergyCapacityChart(props) {
    return (
        <QueryClientProvider client={new QueryClient()}>
            <EnergyCapacityChartCore/>
        </QueryClientProvider>
    );
}


function EnergyCapacityChartCore(props) {
    const dataFetchFunc = async () => {
        const { data } = await axios.get(
            'https://dummyjson.com/carts'
        );
        return data;
    };

    const time = [];
    const actualCapacity = [];
    const clearedCapacity = [6000, 2000, 3874, 1943, 3984, 8237, 4720, 3975, 8237, 2332, 4038];
    const {
        isLoading,
        isSuccess,
        error,
        isError,
        data: energyCapacityData
    } = useQuery("energyCapacity", dataFetchFunc, {refetchInterval: 300000});
    if (isSuccess) {
        for (let i = 0; i < energyCapacityData.carts.length; i++) {
            time[i] = energyCapacityData.carts[i].id;
            actualCapacity[i] = energyCapacityData.carts[i].total;
        }
    }

    let energyCapacityChart = {
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
                        borderColor: "#1ff1b9",
                        borderWidth: 2,
                        borderDash: [],
                        borderDashOffset: 0.0,
                        pointBackgroundColor: "#1ff1b9",
                        pointBorderColor: "rgba(255,255,255,0)",
                        pointHoverBackgroundColor: "#1ff1b9",
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
        options: energyCapacityChartOption
    };

    return (
        <Line
            data={energyCapacityChart.data}
            options={energyCapacityChart.options}
        />
    );
}

export default EnergyCapacityChart;
