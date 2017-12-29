/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var QuestionsIdPublic = function () {
    /*
        @params obj 'data params'
            id   'string' string id in path
            is_public   'boolean' 
            is_notice   'boolean' 
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
            url: "/questions/" + obj.id + "/public",
            method: "PUT",
            data: {
                is_public: obj.is_public,
                is_notice: obj.is_notice,
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
    QuestionsIdPublic: new QuestionsIdPublic
};