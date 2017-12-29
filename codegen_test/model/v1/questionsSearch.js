/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var QuestionsSearch = function () {
    /*
        @params obj 'data params'
            kw   'string' key word in query
            offset   'integer' offset number
            limit   'integer' limit number
            page   'integer' page number
            per_page   'integer' per_page number
            
        @success
            status 200    type:array
            content   'ref' 
            respondent   'ref' 
            type   'ref' 
            id   'ref' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/questions/search",
            method: "GET",
            data: {
                kw: obj.kw,
                offset: obj.offset,
                limit: obj.limit,
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
    QuestionsSearch: new QuestionsSearch
};