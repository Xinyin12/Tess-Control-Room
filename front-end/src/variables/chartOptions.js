const systemLoadChartOption = {
    maintainAspectRatio: false,
    legend: {
        display: false
    },
    tooltips: {
        backgroundColor: "#f5f5f5",
        titleFontColor: "#333",
        bodyFontColor: "#666",
        bodySpacing: 4,
        xPadding: 12,
        mode: "nearest",
        intersect: 0,
        position: "nearest"
    },
    responsive: true,
    scales: {
        yAxes: [
            {
                scaleLabel: {
                    display: true,
                    labelString: 'probability'
                },
                barPercentage: 1.6,
                gridLines: {
                    drawBorder: false,
                    color: "rgba(29,140,248,0.0)",
                    zeroLineColor: "transparent"
                },
                ticks: {
                    suggestedMin: 60,
                    suggestedMax: 125,
                    padding: 20,
                    fontColor: "#9a9a9a"
                },
            }
        ],
        xAxes: [
            {
                barPercentage: 1.6,
                gridLines: {
                    drawBorder: false,
                    color: "rgb(224,198,96)",
                    zeroLineColor: "transparent"
                },
                ticks: {
                    padding: 20,
                    fontColor: "#9a9a9a",
                    autoSkip: false,
                    maxRotation: 90,
                    minRotation: 90
                }
            }
        ]
    }
};

const energyCapacityChartOption = {

}

const auctionMarketChartOption = {

}

const realtimePowerChartOption = {

}

const realtimeEnergyChartOption = {

}

const TERPriceLoadForecastChartOption = {

}

module.exports = {
    systemLoadChartOption,
    energyCapacityChartOption,
    auctionMarketChartOption,
    realtimeEnergyChartOption,
    realtimePowerChartOption,
    TERPriceLoadForecastChartOption
};
