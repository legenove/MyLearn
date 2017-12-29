/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var TalksIdRepliesReplyId = function () {
    /*
        @params obj 'data params'
            id   'string' string id in path
            id   'string' reply id in path
            is_digest   'boolean' 
            
        @success
            status 200    type:object
            question   'ref' 
            respondent   'ref' 
            id   'ref' 
            is_digest   'boolean' 
            question_id   'ref' 
            
    */
    this.put = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/talks/" + obj.id + "/replies/<<reply_id>>",
            method: "PUT",
            data: {
                is_digest: obj.is_digest
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
    TalksIdRepliesReplyId: new TalksIdRepliesReplyId
};