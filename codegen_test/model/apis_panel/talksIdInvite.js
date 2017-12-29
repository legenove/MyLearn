/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var TalksIdInvite = function () {
    /*
        @params obj 'data params'
            id   'string' string id in path
            account_ids   'array' 
            
        @success
            status 201    type:object
            ok   'boolean' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/talks/" + obj.id + "/invite",
            method: "POST",
            data: {
                account_ids: obj.account_ids
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
    TalksIdInvite: new TalksIdInvite
};