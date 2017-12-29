/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var Gquestions = function () {
    /*
        @params obj 'data params'
            status   'string' status in query
            asker_nickname   'string' nickname in query
            respondent_nickname   'string' nickname in query
            interval_from_succeed   'integer' interval in query
            order_by   'string' order by in query
            limit   'integer' limit number
            offset   'integer' offset number
            page   'integer' page number
            per_page   'integer' per_page number
            
        @success
            status 200    type:array
            status   'ref' 
            asker   'ref' 
            respondent   'ref' 
            account_id   'integer' 
            offer   'integer' 
            date_updated   'string' 
            respondent_id   'integer' 
            content   'string' 
            is_public   'boolean' 
            date_created   'string' 
            id   'string' 
            visitor_count   'integer' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/gquestions",
            method: "GET",
            data: {
                status: obj.status,
                asker_nickname: obj.asker_nickname,
                respondent_nickname: obj.respondent_nickname,
                interval_from_succeed: obj.interval_from_succeed,
                order_by: obj.order_by,
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
    Gquestions: new Gquestions
};