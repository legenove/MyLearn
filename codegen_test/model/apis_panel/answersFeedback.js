/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var AnswersFeedback = function () {
    /*
        @params obj 'data params'
            account_id   'integer' account id in query
            respondent_id   'integer' respondent id in query
            limit   'integer' limit number
            offset   'integer' offset number
            page   'integer' page number
            per_page   'integer' per_page number
            
        @success
            status 200    type:array
            content   'string' 
            score   'integer' 
            respondent   'ref' 
            account_id   'integer' 
            question_id   'string' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/answers/feedback",
            method: "GET",
            data: {
                account_id: obj.account_id,
                respondent_id: obj.respondent_id,
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
    AnswersFeedback: new AnswersFeedback
};