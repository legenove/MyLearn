/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var BatchQuestions = function () {
    /*
        @params obj 'data params'
            question_id   'array' question ids in query
            
        @success
            status 200    type:array
            status   'ref' 
            listenings_count   'ref' 
            offer   'ref' 
            respondent_id   'ref' 
            review_status   'ref' 
            content   'ref' 
            is_public   'boolean' 
            date_created   'ref' 
            type   'ref' 
            id   'ref' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/batch/questions",
            method: "GET",
            data: {
                question_id: obj.question_id
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
    BatchQuestions: new BatchQuestions
};