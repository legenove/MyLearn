/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var QuestionsIdTopups = function () {
    /*
        @params obj 'data params'
            id   'string' string id in path
            duration   'integer' 
            date_executed   'string' 
            visitor_count   'integer' 
            
        @success
            status 200    type:object
            operator_id   'ref' 
            account_id   'ref' 
            respondent_id   'ref' 
            date_created   'ref' 
            visitor_count   'integer' 
            id   'ref' 
            question_id   'ref' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/questions/" + obj.id + "/topups",
            method: "POST",
            data: {
                duration: obj.duration,
                date_executed: obj.date_executed,
                visitor_count: obj.visitor_count
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
    QuestionsIdTopups: new QuestionsIdTopups
};