/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var PartnerQuestionsIdAnswer = function () {
    /*
        @params obj 'data params'
            id   'string' question id in path
            
        @success
            status 200    type:object
            duration   'integer' 
            likings_count   'integer' 
            voice   'string' 
            voice_id   'string' 
            question_id   'ref' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/partner/questions/" + obj.id + "/answer",
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
    

};

module.exports = {
    PartnerQuestionsIdAnswer: new PartnerQuestionsIdAnswer
};