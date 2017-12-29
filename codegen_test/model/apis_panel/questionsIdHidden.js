/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var QuestionsIdHidden = function () {
    /*
        @params obj 'data params'
            id   'string' string id in path
            is_hidden   'boolean' 
            reason   'string' 
            
        @success
            status 200    type:object
            status   'ref' 
            asker   'ref' 
            offer   'ref' 
            respondent_id   'ref' 
            review_status   'ref' 
            content   'ref' 
            is_public   'boolean' 
            date_created   'ref' 
            type   'ref' 
            id   'ref' 
            
    */
    this.put = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/questions/" + obj.id + "/hidden",
            method: "PUT",
            data: {
                is_hidden: obj.is_hidden,
                reason: obj.reason
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
    QuestionsIdHidden: new QuestionsIdHidden
};