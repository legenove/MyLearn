/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var AppSelfQuestionsReceived = function () {
    /*
        @params obj 'data params'
            status   'string' status in query
            answer_filter   'string' filter in query
            limit   'integer' limit number
            offset   'integer' offset number
            page   'integer' page number
            per_page   'integer' per_page number
            
        @success
            status 200    type:array
            bonuses   'integer' 
            is_fenda_ask   'boolean' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/app/self/questions/received",
            method: "GET",
            data: {
                status: obj.status,
                answer_filter: obj.answer_filter,
                limit: obj.limit,
                offset: obj.offset,
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
    AppSelfQuestionsReceived: new AppSelfQuestionsReceived
};