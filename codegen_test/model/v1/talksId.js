/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var TalksId = function () {
    /*
        @params obj 'data params'
            id   'string' string id in path
            
        @success
            status 200    type:object
            listenings_count   'integer' 
            description   'string' 
            is_sticky   'boolean' 
            introduction   'string' 
            image   'string' 
            date_updated   'ref' 
            share_description   'string' 
            share_title   'string' 
            is_hot   'boolean' 
            answers_count   'integer' 
            guide   'string' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/talks/" + obj.id + "",
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
    TalksId: new TalksId
};