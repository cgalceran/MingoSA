$(function() {

    Morris.Area({
        element: 'morris-area-chart',
        data: [{
            period: '2010 Q1',
            Radiadores: 2666,
            Motores: null,
            itouch: 2647
        }, {
            period: '2010 Q2',
            Radiadores: 2778,
            Motores: 2294,
            itouch: 2441
        }, {
            period: '2010 Q3',
            Radiadores: 4912,
            Motores: 1969,
            itouch: 2501
        }, {
            period: '2010 Q4',
            Radiadores: 3767,
            Motores: 3597,
            itouch: 5689
        }, {
            period: '2011 Q1',
            Radiadores: 6810,
            Motores: 1914,
            itouch: 2293
        }, {
            period: '2011 Q2',
            Radiadores: 5670,
            Motores: 4293,
            itouch: 1881
        }, {
            period: '2011 Q3',
            Radiadores: 4820,
            Motores: 3795,
            itouch: 1588
        }, {
            period: '2011 Q4',
            Radiadores: 15073,
            Motores: 5967,
            itouch: 5175
        }, {
            period: '2012 Q1',
            Radiadores: 10687,
            Motores: 4460,
            itouch: 2028
        }, {
            period: '2012 Q2',
            Radiadores: 8432,
            Motores: 5713,
            itouch: 1791
        }],
        xkey: 'period',
        ykeys: ['Radiadores', 'Motores', 'itouch'],
        labels: ['Radiadores', 'Motores', 'iPod Touch'],
        pointSize: 2,
        hideHover: 'auto',
        resize: true
    });

    Morris.Donut({
        element: 'morris-donut-chart',
        data: [{
            label: "Download Sales",
            value: 12
        }, {
            label: "In-Store Sales",
            value: 30
        }, {
            label: "Mail-Order Sales",
            value: 20
        }],
        resize: true
    });

    Morris.Bar({
        element: 'morris-bar-chart',
        data: [{
            y: '2006',
            a: 100,
            b: 90
        }, {
            y: '2007',
            a: 75,
            b: 65
        }, {
            y: '2008',
            a: 50,
            b: 40
        }, {
            y: '2009',
            a: 75,
            b: 65
        }, {
            y: '2010',
            a: 50,
            b: 40
        }, {
            y: '2011',
            a: 75,
            b: 65
        }, {
            y: '2012',
            a: 100,
            b: 90
        }],
        xkey: 'y',
        ykeys: ['a', 'b'],
        labels: ['Series A', 'Series B'],
        hideHover: 'auto',
        resize: true
    });

});
