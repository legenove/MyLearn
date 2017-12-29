/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var QuestionsNext = function () {
    /*
        @params obj 'data params'
            question_id   'string' question id in query
            target   'string' target in query
            target_type   'string' target type in query
            
        @success
            status 200    type:object
            source   'string' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/questions/next",
            method: "GET",
            data: {
                question_id: obj.question_id,
                target: obj.target,
                target_type: obj.target_type
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
    QuestionsNext: new QuestionsNext
};