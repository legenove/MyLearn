/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var Topline = function () {
    /*
        @params obj 'data params'
            type   'string' 分答头条参数
            offset   'integer' offset number
            limit   'integer' limit number
            page   'integer' page number
            per_page   'integer' per_page number
            
        @success
            status 200    type:array
            respondent   'ref' 
            album_id   'string' 
            date_updated   'ref' 
            question   'ref' 
            short_title   'string' 短标题
            answer   'ref' 
            id   'string' 
            question_id   'string' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/topline",
            method: "GET",
            data: {
                type: obj.type,
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
    Topline: new Topline
};