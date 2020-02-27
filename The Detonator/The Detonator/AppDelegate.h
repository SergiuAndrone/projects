//
//  AppDelegate.h
//  The Detonator
//
//  Created by sergiuandrone on 28/11/2019.
//  Copyright © 2019 sergiuandrone. All rights reserved.
//

#import <Cocoa/Cocoa.h>
#import "Samples.h"

@interface AppDelegate : NSObject <NSApplicationDelegate>

@property (weak) IBOutlet NSTextField *samplesNumber;
@property (weak) IBOutlet NSTextField *samplesDropped;
@property (weak) IBOutlet NSProgressIndicator *progressBar;
@property int totalCount;
@property (weak) IBOutlet NSTextField *Destination;

-(NSString*)validateDestination;

- (IBAction)dropbatTrojan:(id)sender;
- (IBAction)dropEicar:(id)sender;
- (IBAction)dropCleanable:(id)sender;
- (IBAction)dropDialer:(id)sender;
- (IBAction)dropKeylogger:(id)sender;
- (IBAction)dropSmartdb:(id)sender;
- (IBAction)dropPacked:(id)sender;
- (IBAction)dropPUA:(id)sender;
- (IBAction)dropAdware:(id)sender;
- (IBAction)dropSpyware:(id)sender;
- (IBAction)dropApplication:(id)sender;
- (IBAction)dropSuspected:(id)sender;
- (IBAction)dropSignedSuspected:(id)sender;
- (IBAction)dropSignedInfected:(id)sender;
- (IBAction)dropMalwareEDR:(id)sender;
- (IBAction)executeRCAPocEdr:(id)sender;
- (IBAction)executePocHttpEDR:(id)sender;
- (IBAction)executeSudospawnATC:(id)sender;

@end

