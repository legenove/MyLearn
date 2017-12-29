/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var LibrariesIdQuestions = function () {
    /*
        @params obj 'data params'
            id   'string' string id in path
            is_digest   'boolean' question id in query
            question_id   'string' question id in query
            status   'string' status in query
            respondent_is_star   'boolean' is star in query
            respondent_is_verified   'boolean' is verified in query
            answer_duration   'integer' duration in query
            order_by   'string' order by in query
            page   'integer' page number
            per_page   'integer' per_page number
            offset   'integer' offset number
            limit   'integer' limit number
            
        @success
            status 200    type:array
            question   'ref' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/libraries/" + obj.id + "/questions",
            method: "GET",
            data: {
                is_digest: obj.is_digest,
                question_id: obj.question_id,
                status: obj.status,
                respondent_is_star: obj.respondent_is_star,
                respondent_is_verified: obj.respondent_is_verified,
                answer_duration: obj.answer_duration,
                order_by: obj.order_by,
                page: obj.page,
                per_page: obj.per_page,
                offset: obj.offset,
                limit: obj.limit
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
    LibrariesIdQuestions: new LibrariesIdQuestions
};