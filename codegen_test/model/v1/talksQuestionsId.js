/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var TalksQuestionsId = function () {
    /*
        @params obj 'data params'
            id   'string' string id in path
            
        @success
            status 200    type:object
            library_id   'ref' 
            respondent_id   'integer' 
            question_id   'ref' 
            recommendation   'string' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/talks/questions/" + obj.id + "",
            method: "GET",
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
    
    /*
        @params obj 'data params'
            id   'string' string id in path
            recommendation   'string' 
            
        @success
            status 200    type:object
            library_id   'ref' 
            respondent_id   'integer' 
            question_id   'ref' 
            recommendation   'string' 
            
    */
    this.put = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/talks/questions/" + obj.id + "",
            method: "PUT",
            data: {
                recommendation: obj.recommendation
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
    TalksQuestionsId: new TalksQuestionsId
};