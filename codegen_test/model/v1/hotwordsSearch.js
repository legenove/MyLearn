/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var HotwordsSearch = function () {
    /*
        @params obj 'data params'
            date_time   'string' 指定时间 格式为 '2016-01-01'
            page   'integer' page number
            per_page   'integer' per_page number
            
        @success
            status 200    type:array
            None   'string' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/hotwords/search",
            method: "GET",
            data: {
                date_time: obj.date_time,
                page: obj.page,
                per_page: obj.per_page
                },
            success: function (res) {
                typeof obj.success === 'function' && obj.success(res);
            },
            fail: function (res) {
                typeof obj.fail === 'function' && obj.fail(res);
            },
            complete: function (res) {
                typeof obj.complete === 'function' && obj.complete(res);
            }
        })
    };
    

};

module.exports = {
    HotwordsSearch: new HotwordsSearch
};