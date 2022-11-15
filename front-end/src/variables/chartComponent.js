import React from "react";
let option = {
    plugins: {
        title: {
            display: false,
            text: 'Chart.js Bar Chart - Stacked',
        },
    },
    responsive: true,
    scales: {
        x: {
            title: {
                display: false,
                text: 'Chart.js Bar Chart - Stacked',
            },
            stacked: true,
        },
        y: {
            title: {
                display: true,
                text: 'Chart.js Bar Chart - Stacked',
            },
            stacked: true,
        },
    },
}

let chartExample3 = {
    data: (canvas) => {
        let ctx = canvas.getContext("2d");

        let gradientStroke = ctx.createLinearGradient(0, 230, 0, 50);

        gradientStroke.addColorStop(1, "rgba(72,72,176,0.1)");
        gradientStroke.addColorStop(0.4, "rgba(72,72,176,0.0)");
        gradientStroke.addColorStop(0, "rgba(119,52,169,0)"); //purple colors

        return {
            labels: ["Total Demand", "Total Supply", "HVACs", "Solar Panels", "Batteries Demand", "Batteries Supply", "EV Chargers", "Water Heaters"],
            datasets: [
                {
                    label: "Dispatched",
                    fill: true,
                    // backgroundColor: gradientStroke,
                    backgroundColor: 'rgb(229,220,123)',
                    hoverBackgroundColor: gradientStroke,
                    borderColor: "#ffffff",
                    borderWidth: 2,
                    borderDash: [],
                    borderDashOffset: 0.0,
                    data: [53, 20, 46, 80, 100, 45]
                },
                {
                    label: "Available",
                    fill: true,
                    // backgroundColor: gradientStroke,
                    backgroundColor: 'rgb(17,231,85)',
                    hoverBackgroundColor: gradientStroke,
                    borderColor: "#ffffff",
                    borderWidth: 2,
                    borderDash: [],
                    borderDashOffset: 0.0,
                    data: [53, 34, 10, 80, 100, 45]
                },
                {
                    label: "Unavailable",
                    fill: true,
                    backgroundColor: gradientStroke,
                    hoverBackgroundColor: gradientStroke,
                    borderColor: "#ffffff",
                    borderWidth: 2,
                    borderDash: [],
                    borderDashOffset: 0.0,
                    data: [53, 15, 27, 80, 100, 45]
                }
            ]
        };
    },
    // options: {
    //     maintainAspectRatio: false,
    //     legend: {
    //         display: false
    //     },
    //     tooltips: {
    //         backgroundColor: "#f5f5f5",
    //         titleFontColor: "#333",
    //         bodyFontColor: "#666",
    //         bodySpacing: 4,
    //         xPadding: 12,
    //         mode: "nearest",
    //         intersect: 0,
    //         position: "nearest"
    //     },
    //     responsive: true,
    //     plugins: {
    //         stacked100: { enable: true },
    //     },
    //     scales: {
    //         yAxes: [
    //             {
    //                 gridLines: {
    //                     drawBorder: false,
    //                     color: "rgba(225,78,202,0.1)",
    //                     zeroLineColor: "transparent"
    //                 },
    //                 ticks: {
    //                     suggestedMin: 60,
    //                     suggestedMax: 120,
    //                     padding: 20,
    //                     fontColor: "#9e9e9e"
    //                 }
    //             }
    //         ],
    //         xAxes: [
    //             {
    //                 gridLines: {
    //                     drawBorder: false,
    //                     color: "rgba(225,78,202,0.1)",
    //                     zeroLineColor: "transparent"
    //                 },
    //                 ticks: {
    //                     padding: 20,
    //                     fontColor: "#9e9e9e"
    //                 }
    //             }
    //         ]
    //     }
    // }
    options: option,
};

export default chartExample3;

// module.exports = {
//     ChartData,
//     chartExample3
// };



